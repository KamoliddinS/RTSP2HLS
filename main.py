
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, BackgroundTasks, HTTPException
import subprocess
import os

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
HLS_DIR = "hls"
os.makedirs(HLS_DIR, exist_ok=True)

@app.post("/convert/")
async def convert_rtsp_to_hls(background_tasks: BackgroundTasks, rtsp_url: str ="rtsp://192.168.1.105:8554/stream"):
    stream_id =hash(rtsp_url)

    if stream_id < 0:
        stream_id=stream_id*-1
    stream_dir = f"{HLS_DIR}/{stream_id}"
    os.makedirs(stream_dir, exist_ok=True)

    background_tasks.add_task(run_ffmpeg, rtsp_url, stream_dir)

    hls_url = f"http://127.0.0.1:8000/hls/{stream_id}/index.m3u8"
    return {"hls_url": hls_url}

def run_ffmpeg(rtsp_url, output_dir):
    cmd = [
        'ffmpeg',
        '-loglevel', 'debug',
        # '-rtsp_transport', 'tcp',
        '-i', rtsp_url,

        '-vsync', '0',       # Disable video sync
        '-copyts',          # Copy timestamps from input to output
        '-vcodec', 'copy',  # Copy codec
        '-hls_segment_type', 'mpegts',
        '-movflags', 'frag_keyframe+empty_moov',
        '-an',
        # '-hls_flags', 'delete_segments+append_list'
        '-f', 'hls',         # HLS format
        '-hls_time', '2',    # Segment duration
        '-hls_list_size', '3',
        '-hls_segment_type', 'mpegts',
        f'{output_dir}/index.m3u8'
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")

# Serve HLS segments and playlist
app.mount("/hls", StaticFiles(directory=HLS_DIR), name="hls")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

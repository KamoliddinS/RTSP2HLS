
# RTSP to HLS Streaming Server

This application is a simple server implemented using FastAPI. It is designed to convert video streams from RTSP (Real Time Streaming Protocol) to HLS (HTTP Live Streaming) format. HLS allows for the efficient streaming of video over HTTP, making it easier to distribute and consume video content over the web.

## Features

- **RTSP to HLS Conversion**: Converts RTSP streams to HLS format, allowing for wider compatibility and easier streaming over the web.
- **Dynamic Stream Handling**: Supports the dynamic conversion of RTSP streams by accepting RTSP URLs via an API endpoint.
- **HLS File Serving**: Serves HLS segments and playlist files using FastAPI's static file serving capabilities.

## Requirements

- Python 3.9+
- FastAPI
- FFmpeg

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/KamoliddinS/RTSP2HLS
   cd RTSP2HLS
   ```

2. **Install Dependencies**

   Make sure you have Python 3.9 or newer installed. Then, install the required Python packages:

   ```bash
   pip install fastapi uvicorn
   ```

   Additionally, ensure FFmpeg is installed on your system. You can download it from [FFmpeg's official site](https://ffmpeg.org/download.html).

## Running the Server

1. **Start the Server**

   Run the following command to start the FastAPI server:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

   Replace `main` with the name of your Python script.

2. **Access the Server**

   The server will be available at `http://127.0.0.1:8000`. You can interact with it using a web browser or tools like `curl`.

## Usage

1. **Convert an RTSP Stream to HLS**

   Send a POST request to the `/convert/` endpoint with the RTSP URL:

   ```bash
   curl -X POST "http://127.0.0.1:8000/convert/" -d "rtsp_url=rtsp://your_rtsp_url_here"
   ```

2. **Accessing the HLS Stream**

   The response will contain an HLS URL which you can use in any HLS-compatible video player.


## Contributing
- **Error Handling and Logging**: Instructions on enhancing error handling and logging mechanisms.
- **FFmpeg Process Management**: Ideas for better process management and resource utilization.
- **HLS Configuration and Optimization**: Suggestions for optimizing HLS streaming.
- **Network and Stream Quality**: Guidelines for network stability improvements and QoS monitoring.
- **Security Enhancements**: Best practices and methods to enhance security.
- **User Interface and Experience**: Proposals for improving API documentation and user feedback mechanisms.
- **Scalability and Performance**: Strategies for scaling and improving performance.
- **CORS Policy Review**: Recommendations for a more secure CORS setup.
- **Storage Management**: Solutions for managing and cleaning up stored HLS files.
- **Configuration and Flexibility**: Ideas for dynamic configuration implementation.
- **Client-Side Player Support**: Suggestions for ensuring compatibility with various HLS players.
- **Monitoring and Health Checks**: Methods for integrating monitoring tools and stream health checks.
- **Documentation and Examples**: Contributions to improve documentation, examples, and troubleshooting guides.



## Notes

- The server is configured with CORS (Cross-Origin Resource Sharing) to allow requests from any origin. Adjust the CORS settings in production environments according to your security requirements.
- The application uses subprocess to run FFmpeg commands. Ensure that your server environment has proper permissions and resources to execute these commands.


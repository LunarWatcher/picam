from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2
from fastapi.responses import FileResponse, StreamingResponse
import asyncio

from contextlib import asynccontextmanager

import fastapi

cam = None

@asynccontextmanager
async def context(app):
    global cam
    print("Connecting camera...")
    cam = Picamera2()
    cam.configure(cam.create_video_configuration(
        main = { "size": (1920, 1080) }
    ))

    # output = MTOutput(frameCallback = broadcast)
    output = FfmpegOutput(
        "-f hls -hls_time 5 -hls_list_size 5 -hls_flags delete_segments -fflags nobuffer -hls_allow_cache 0 stream.m3u8"
    )
    encoder = H264Encoder()

    cam.start_recording(
        encoder,
        output,
        quality = Quality.HIGH
    )
    yield
    print("Killing camera")

    cam.close()
    cam = None

app = fastapi.FastAPI(lifespan = context)

@app.get("/stream.m3u8")
def readStream():
    return FileResponse(
        f"./stream.m3u8",
        media_type="application/x-mpegURL"
    )


@app.get("/stream{segment}.ts")
def readSegment(segment: int):
    return FileResponse(
        f"./stream{segment}.ts",
        media_type="application/x-mpegURL"
    )


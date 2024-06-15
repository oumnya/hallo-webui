import gradio as gr
import subprocess
from datetime import datetime
import os
import platform

def generate_video(ref_img, ref_audio):
    # Ensure file paths are correct
    if not os.path.isfile(ref_img) or not os.path.isfile(ref_audio):
        return "Error: File not found", None

    # Path to the output video file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # Check if output exists and if not create it
    if not os.path.exists("output"):
        os.makedirs("output")
    
    output_video = f"output/{timestamp}.mp4"

    # Determine the command based on the operating system
    if platform.system() == "Windows":
        command = f"venv\\Scripts\\activate && python scripts\\inference.py --source_image {ref_img} --driving_audio {ref_audio} --output {output_video}"
    else:
        command = f"source venv/bin/activate && python scripts/inference.py --source_image {ref_img} --driving_audio {ref_audio} --output {output_video}"

    try:
        # Execute the command
        result = subprocess.run(command, shell=True, check=True)

        if result.returncode == 0:
            return "Video generated successfully", output_video
        else:
            return "Error generating video", None

    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}", None

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            ref_img = gr.Image(label="Reference Image", type="filepath")
            ref_audio = gr.Audio(label="Audio", type="filepath")
        with gr.Column():
            result_status = gr.Label(value="Status")
            result_video = gr.Video(label="Result Video", interactive=False)
            result_btn = gr.Button(value="Generate Video")

    result_btn.click(fn=generate_video, inputs=[ref_img, ref_audio], outputs=[result_status, result_video])

if __name__ == "__main__":
    demo.queue()
    demo.launch(inbrowser=True,share=True)

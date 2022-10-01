import gradio as gr

from descriptions import TABS
from descriptions import DOCUMENTATION
from utils import invert_text

with gr.Blocks() as interface:
    # Set title and description
    gr.Markdown("""
        # Save the Earth from Another Carrington Event! 🌎
    """)

    # Project description and app instructions
    with gr.Row():
        with gr.Tab("Challenge"):
            gr.Markdown(TABS['challenge'])
        with gr.Tab("Solution"):
            gr.Markdown(TABS['solution'])
        with gr.Tab("Instructions"):
            gr.Markdown(TABS['instructions'])

    # Main interface
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Data input")
            text_input = gr.Textbox()
            text_button = gr.Button("Flip")
        with gr.Column():
            gr.Markdown("### Output")
            text_output = gr.Textbox()

    # Project documentation
    gr.Markdown(DOCUMENTATION)

    # Button to run model
    text_button.click(invert_text, inputs=text_input, outputs=text_output)

interface.launch(show_api=False, share=True)

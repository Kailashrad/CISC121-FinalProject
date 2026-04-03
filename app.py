import gradio as gr

def run_sort_demo(user_input):
    if not user_input.strip():
        return "Please enter some values."

    values = [x.strip() for x in user_input.split(",")]
    return f"You entered: {values}"

demo = gr.Interface(
    fn=run_sort_demo,
    inputs=gr.Textbox(label="Enter values separated by commas"),
    outputs=gr.Textbox(label="Output"),
    title="Sorting Project Demo",
    description="This is my starter Gradio app for my sorting project."
)

if __name__ == "__main__":
    demo.launch()
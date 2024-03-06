import gradio as gr
import openai

openai.api_key = "Enter your Api-Key"

def gen(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Human:{message}",
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    #stop=[" Human:", " AI:"]
  )
  return(response.choices[0].text)
with gr.Blocks() as demo:
          input_text = gr.inputs.Textbox(label="input_1")
          output_text = gr.outputs.Textbox(label="Output_1")
          btn = gr.Button("Click")
          btn.click(fn = gen, inputs=input_text, outputs = output_text)
demo.launch()

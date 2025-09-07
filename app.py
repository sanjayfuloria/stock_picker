
import gradio as gr
from src.stock_picker.main import run

def pick_stock(sector):
    result = run(sector)
    return str(result)

iface = gr.Interface(
    fn=pick_stock,
    inputs=gr.Dropdown(
        choices=["Technology", "Consumer Goods", "Retail", "Energy"],
        label="Sector",
        value="Technology"
    ),
    outputs="text",
    title="Stock Picker"
)

if __name__ == "__main__":
    iface.launch()

<<<<<<< HEAD
# stock_picker
This analyses companies in the given sector and suggests where to invest.
=======
<<<<<<< HEAD
# stock_picker
This analyses companies in the given sector and suggests where to invest.
=======
# StockPicker Crew

Welcome to the StockPicker Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/stock_picker/config/agents.yaml` to define your agents
- Modify `src/stock_picker/config/tasks.yaml` to define your tasks
- Modify `src/stock_picker/crew.py` to add your own logic, tools and specific args
- Modify `src/stock_picker/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the stock_picker Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## How to run locally

```sh
pip install -r requirements.txt
python app.py
```

## Deploy to Hugging Face Spaces

1. Push your project (including `requirements.txt`, `app.py`, and your code) to a public GitHub repository.
2. Go to [Hugging Face Spaces](https://huggingface.co/spaces) and click "Create new Space".
3. Choose "Gradio" as the Space type.
4. Link your GitHub repo or upload the files directly.
5. Set your environment variables (API keys) in the Space settings if needed.
6. Your app will build and launch automatically!

## Example Hugging Face Space Settings

- **Space type:** Gradio
- **Python version:** 3.10+
- **Environment variables:**
  - `OPENAI_API_KEY` (if needed)
  - `BRAVE_API_KEY` (required for BraveSearchTool)

## Troubleshooting

- Make sure all dependencies are listed in `requirements.txt`.
- If you see missing package errors, add them to `requirements.txt` and re-push.
- For API key errors, set the keys in the Space settings (not in `.env`).

## Understanding Your Crew

The stock_picker Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the StockPicker Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
>>>>>>> 9faf2d28 (Initial commit for Hugging Face Spaces)
>>>>>>> 89e9287 (Initial commit for Hugging Face Spaces)

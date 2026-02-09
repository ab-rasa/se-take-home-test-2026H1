# Rasa Solution Engineer - Take Home Test - 2026H1
Rasa Solution Engineer Applicant

## Preparation Instructions

Your task is to work with a Retail AI Agent capable of handling money transfers and other common banking transactions.

As part of this technical take-home exercise, you will be given a Retail AI Agent that contains several intentional issues. Your goal is to debug the existing implementation and extend the assistant by adding additional skills.

You will have **three business days** to complete the exercise.

This take-home will be reviewed by a Rasa Engineer. Your approach, decisions, and improvements will be discussed during a follow-up technical interview.

## What We Are Evaluating

Approach this exercise as you would a real customer or production scenario. We are evaluating:

- Your understanding of the Rasa platform
- Your technical depth and correctness
- Your ability to diagnose and resolve issues logically
- Your resourcefulness and use of available documentation
- Your ability to clearly explain, present and demo your work creatively

## Getting Started

To prepare, review the **Rasa Pro** documentation:  
https://rasa.com/docs/pro/intro/

You will need:

- A **Rasa Pro Developer Edition** license
- An **OpenAI API key** (GPT-4o)

Request a Rasa Pro Developer Edition license here:  
https://rasa.com/rasa-pro-developer-edition-license-key-request

OpenAI configuration details are available here:  
https://rasa.com/docs/reference/config/components/llm-configuration/#openai

## Familiarity with Rasa

- **If you are already familiar with Rasa**  
  - Review the files in this repository, starting with this README.

- **If you are new to Rasa, we recommend**:
  - Installing Rasa Pro locally and completing the prerequisite setup steps below
  - Reviewing key concepts, starting with flows:  
    https://rasa.com/docs/reference/primitives/flows/
  - Reviewing the Rasa Command Line Interface:  
    https://rasa.com/docs/reference/api/command-line-interface/
  - Reading this README in full

## Prerequisites

You will need the following tools installed locally to run this project:
- **Homebrew**: Package manager for macOS
- **pyenv**: Python version management
- **uv**: Fast Python package installer and dependency resolver

## Setup

1. Install and set up **Rasa Pro**:  
   https://rasa.com/docs/pro/installation/python
2. Confirm your Rasa version is **3.15.9 or later**.

> **Note**  
> Ensure your Rasa license key and OpenAI API key are set as environment variables within your virtual environment.

## Usage

### Rasa Pro Workflow

A typical local workflow looks like:
1. Clean existing models and logs
2. Train and validate the Rasa model
3. Start the Rasa Inspector

## Project Structure

Below is a brief overview of the directories and files in the project root:

- `README.md`: Instructions and context for the take-home exercise
- `actions/`: Python code defining custom actions for the assistant
- `configs/`: Configuration files for different language models and runtime settings
- `credentials.yml`: Credentials for external services used by the assistant
- `custom/`: Custom Python components imported into the Rasa pipeline
- `data/`: Flow definitions and conversational data
- `docs/`: Sample documents used for Enterprise Search scenarios
- `domain/`: Domain definitions for the assistant
- `e2e_tests/`: End-to-end test scenarios, organized by test suite
- `endpoints.yml`: Endpoint configuration for the assistant
- `prompts/`: Jinja2 templates used for prompt generation
- `requirements.txt`: Python dependencies required for the project







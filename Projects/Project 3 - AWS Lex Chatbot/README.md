# Project 3 – AWS Lex Chatbot

*An interactive chatbot built with Amazon Lex, combining a basic conversational experience with an AWS knowledge quiz.*

## Project Overview

This project was completed as part of the AWS re/Start programme. The objective was to build a chatbot using Amazon Lex and demonstrate how it can respond to user input through intents, sample utterances, and configured responses.

The project follows a two-part brief: first, a basic chatbot; then, an interactive knowledge quiz that uses branching logic to respond to users' answers.

## Chatbot Functionality

### Part 1 – Basic Chatbot

The first part introduces the basic conversational flow:

- A user enters a topic-related question or request.
- Amazon Lex matches the input to the configured intent and sample utterances.
- The chatbot returns the response configured for that intent.

### Part 2 – Interactive Knowledge Quiz

The second part extends the chatbot with a knowledge quiz on an AWS topic.

The quiz presents multiple-choice questions and uses branching logic to handle the user's answers. It provides feedback for correct and incorrect responses, then allows the user to retry or continue to the next question.

## How Amazon Lex Is Used

Amazon Lex provides the conversational interface for the chatbot. Intents identify what the user wants to do, sample utterances provide examples of how a user may express that request, and configured responses guide the conversation.

For the quiz, branching logic connects the user's answer to the appropriate feedback and next step in the interaction.

## AWS Service

| AWS service | Role in the project |
|---|---|
| **Amazon Lex** | Used to create the chatbot, configure intents and sample utterances, and manage responses and quiz interactions. |

## Skills Demonstrated

- Amazon Lex bot configuration
- Intent and sample utterance design
- Conversational flow development
- Branching logic for quiz responses
- Testing chatbot interactions

# FitBuddy - AI Fitness Plan Generator

FitBuddy is an intelligent, full-stack fitness routine and nutrition generation platform built with FastAPI, SQLAlchemy, and Google Gemini AI models.

## Architectural Overview
- **Orchestration**: FastAPI (ASGI Server via Uvicorn)
- **Generative Engine**: Google Gemini 1.5 Pro (7-Day Workout & Iterative Feedback) & Gemini 1.5 Flash (Targeted Nutrition Insights)
- **Persistence**: SQLite with SQLAlchemy ORM
- **Presentation**: Jinja2 Server-Side Templating with modern CSS design
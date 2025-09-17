# Jharkhand Heritage & Journey Planner

## Overview
This project is a beautiful website showcasing Jharkhand's heritage, culture, and providing an AI-powered travel planning experience. It's a static website with two main pages:

1. **Heritage Marketplace** (`h3.0.html`) - Main page showcasing Jharkhand's culture, products, places, and heritage
2. **AI Journey Planner** (`h3.0.1.html`) - Interactive travel planning tool with AI assistance

## Project Structure
```
├── 3.0  copy/
│   ├── h3.0.html      # Main heritage marketplace page
│   └── h3.0.1.html    # AI travel planner page
├── server.py          # Simple HTTP server for serving static files
└── replit.md          # This documentation
```

## Recent Changes
- **Setup (Sept 17, 2025)**: 
  - Created Python HTTP server to serve static HTML files on port 5000
  - Fixed navigation links between pages (removed hardcoded localhost URLs)
  - Added "Back to Heritage" navigation button on the travel planner page
  - Configured deployment settings for production
  - Set up proper caching headers for development

## Features
- **Heritage Marketplace**: Showcases Jharkhand's culture, products, spiritual sites, adventures, cuisine, nature, and festivals
- **AI Travel Planner**: Interactive form-based travel planning with destination selection, budget planning, and AI assistance
- **Responsive Design**: Mobile-friendly with modern glass morphism effects and animations
- **Navigation**: Seamless navigation between both pages

## Development Setup
- **Language**: Python 3.11
- **Port**: 5000 (frontend)
- **Host**: 0.0.0.0 (allows access through Replit's proxy)
- **Framework**: Static HTML/CSS/JavaScript with Tailwind CSS

## Deployment Configuration
- **Target**: Autoscale (suitable for static websites)
- **Run Command**: `python server.py`
- **Features**: No-cache headers for development, proper error handling

## User Preferences
- Static website focused on Jharkhand tourism and heritage
- Modern UI with animations and interactive elements
- AI-powered travel planning functionality
- Mobile-responsive design

## Architecture Notes
- Simple HTTP server serving static files
- No backend database or API dependencies
- Uses CDN resources (Tailwind CSS, Font Awesome)
- Client-side JavaScript for interactive features

## Navigation
- Main page → Travel planner: "Plan Your Destination" button
- Travel planner → Main page: "← Back to Heritage" button

The website is ready for use and deployed to production.
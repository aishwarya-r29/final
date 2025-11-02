# Farm to Factories Exchange

## Overview
AI-powered marketplace web application connecting farmers and factories for sustainable agricultural partnerships. Built with Django and Bootstrap 5.

**Project Created:** November 2, 2025

## Purpose
Support UN Sustainable Development Goals (SDGs):
- SDG 2: Zero Hunger
- SDG 8: Decent Work and Economic Growth
- SDG 9: Industry, Innovation and Infrastructure

## Current State
✅ Fully functional Django web application with 6 pages
✅ Bootstrap 5 responsive design
✅ Dummy data for demonstrations
✅ Running on port 5000

## Project Architecture

### Technology Stack
- **Backend:** Django 5.2.7
- **Frontend:** Django Templates + Bootstrap 5 (via CDN)
- **Styling:** Custom CSS
- **Python:** 3.11

### Directory Structure
```
farm_to_factories_exchange/        # Django project
├── exchange/                       # Main app
│   ├── templates/exchange/        # HTML templates
│   │   ├── base.html              # Base template with navbar/footer
│   │   ├── landing.html           # Welcome page with SDG goals
│   │   ├── farmer_dashboard.html # Farmer batch listings
│   │   ├── factory_dashboard.html # Factory demand listings
│   │   ├── upload_batch.html     # Batch upload form
│   │   ├── post_demand.html      # Demand posting form
│   │   └── matches.html          # AI match results
│   ├── views.py                   # Views with dummy data
│   ├── urls.py                    # App URL configuration
│   └── apps.py                    # App configuration
├── settings.py                    # Django settings
└── urls.py                        # Project URL configuration
static/                            # Static files
├── css/style.css                 # Custom styles
└── logo.svg                      # Application logo
```

## Features Implemented

### Pages and Routes
1. **Landing Page** (`/`) - Welcome page with SDG goals and navigation
2. **Farmer Dashboard** (`/farmer/dashboard/`) - List of farmer batches
3. **Factory Dashboard** (`/factory/dashboard/`) - List of factory demands
4. **Upload Batch** (`/upload_batch/`) - Form to add new batch
5. **Post Demand** (`/post_demand/`) - Form to add new demand
6. **Matches** (`/matches/`) - AI-powered match recommendations

### Data Structure
Currently using in-memory Python lists/dictionaries in `views.py`:
- **FARMER_BATCHES**: Product offerings from farmers
- **FACTORY_DEMANDS**: Product requirements from factories
- **MATCHES**: AI-generated matches with scores and explanations

## Recent Changes
- November 2, 2025: Initial project creation
  - Created Django project structure
  - Configured settings for static files and allowed hosts
  - Implemented all 6 pages with Bootstrap styling
  - Added dummy data for demonstration
  - Configured workflow to run server on port 5000

## Next Phase Suggestions
1. **Persistence**: Add database models and migrations for batches/demands
2. **Authentication**: Implement user login to distinguish farmers from factories
3. **Forms**: Make upload/post forms functional with Django forms
4. **AI Matching**: Implement actual matching algorithm based on product compatibility
5. **CRUD Operations**: Add edit/delete functionality for batches and demands
6. **Messaging**: Add communication system between matched parties
7. **Production**: Configure for deployment with proper secret management

## User Preferences
None specified yet.

## Notes
- Server runs on port 5000 (required for Replit webview)
- Bootstrap 5 loaded via CDN
- No database required for current demo version
- Migrations warning in logs is expected (not using database models yet)

#!/usr/bin/env python
# src/latest_ai_development/main.py
import sys
from crew_test_agent.crew import LatestAiDevelopmentCrew

def run():
  """
  Run the crew.
  """
  inputs = {
    'topic': 'AI Agents'
  }
  LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
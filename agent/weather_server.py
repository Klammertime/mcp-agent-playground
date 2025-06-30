#!/usr/bin/env python3
"""
Weather MCP Server

A custom MCP server that provides weather information tools.
This demonstrates how to create extensible functionality for the MCP agent.
"""

import json
import asyncio
from typing import Any, Dict
from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Weather Server")


@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    Get the current weather for a specified city.
    
    Args:
        city: The name of the city to get weather for
        
    Returns:
        A formatted string with current weather information
    """
    # In a real implementation, you'd call a weather API like OpenWeatherMap
    # For now, we'll return mock data with realistic-looking information
    
    weather_data = {
        "Tokyo": {"temp": "22°C", "condition": "Partly Cloudy", "humidity": "65%", "wind": "12 km/h"},
        "Paris": {"temp": "18°C", "condition": "Light Rain", "humidity": "80%", "wind": "8 km/h"},
        "New York": {"temp": "25°C", "condition": "Sunny", "humidity": "55%", "wind": "15 km/h"},
        "London": {"temp": "16°C", "condition": "Overcast", "humidity": "75%", "wind": "10 km/h"},
        "Sydney": {"temp": "28°C", "condition": "Clear", "humidity": "60%", "wind": "20 km/h"},
    }
    
    # Get weather for the city or provide default
    city_title = city.title()
    weather = weather_data.get(city_title, {
        "temp": "20°C", 
        "condition": "Unknown", 
        "humidity": "60%", 
        "wind": "10 km/h"
    })
    
    return f"""🌤️ Current Weather in {city_title}:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌡️  Temperature: {weather['temp']}
☁️  Condition: {weather['condition']}
💧 Humidity: {weather['humidity']}
💨 Wind Speed: {weather['wind']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


@mcp.tool()
def get_weather_forecast(city: str, days: int = 3) -> str:
    """
    Get a multi-day weather forecast for a specified city.
    
    Args:
        city: The name of the city to get forecast for
        days: Number of days to forecast (default: 3, max: 7)
        
    Returns:
        A formatted string with weather forecast information
    """
    # Limit days to reasonable range
    days = min(max(days, 1), 7)
    
    # Mock forecast data
    forecast_templates = [
        {"temp_high": "24°C", "temp_low": "18°C", "condition": "Sunny", "chance_rain": "10%"},
        {"temp_high": "22°C", "temp_low": "16°C", "condition": "Partly Cloudy", "chance_rain": "25%"},
        {"temp_high": "20°C", "temp_low": "14°C", "condition": "Light Rain", "chance_rain": "70%"},
        {"temp_high": "26°C", "temp_low": "20°C", "condition": "Clear", "chance_rain": "5%"},
        {"temp_high": "19°C", "temp_low": "13°C", "condition": "Overcast", "chance_rain": "40%"},
        {"temp_high": "23°C", "temp_low": "17°C", "condition": "Scattered Showers", "chance_rain": "60%"},
        {"temp_high": "25°C", "temp_low": "19°C", "condition": "Sunny", "chance_rain": "15%"},
    ]
    
    city_title = city.title()
    forecast_text = f"📅 {days}-Day Weather Forecast for {city_title}:\n"
    forecast_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    day_names = ["Today", "Tomorrow", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
    
    for i in range(days):
        day = day_names[i] if i < len(day_names) else f"Day {i+1}"
        forecast = forecast_templates[i % len(forecast_templates)]
        
        forecast_text += f"📆 {day}:\n"
        forecast_text += f"   🌡️  High: {forecast['temp_high']} | Low: {forecast['temp_low']}\n"
        forecast_text += f"   ☁️  {forecast['condition']}\n"
        forecast_text += f"   🌧️  Rain Chance: {forecast['chance_rain']}\n"
        
        if i < days - 1:  # Don't add separator after last day
            forecast_text += "   ────────────────────────────────────────\n"
    
    forecast_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    return forecast_text


@mcp.tool()
def get_weather_alerts(city: str) -> str:
    """
    Get weather alerts and warnings for a specified city.
    
    Args:
        city: The name of the city to check for alerts
        
    Returns:
        A formatted string with weather alerts or "No alerts" message
    """
    # Mock alert data - in real implementation, this would come from weather service
    alerts_data = {
        "Miami": ["🌀 Tropical Storm Watch in effect", "🌊 Coastal Flood Advisory"],
        "Phoenix": ["🔥 Excessive Heat Warning", "💨 Dust Storm Advisory"],
        "Denver": ["❄️ Winter Weather Advisory", "🌨️ Heavy Snow Warning"],
        "San Francisco": ["🌫️ Dense Fog Advisory"],
    }
    
    city_title = city.title()
    alerts = alerts_data.get(city_title, [])
    
    if not alerts:
        return f"✅ No weather alerts for {city_title} at this time."
    
    alert_text = f"⚠️  Weather Alerts for {city_title}:\n"
    alert_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    for i, alert in enumerate(alerts, 1):
        alert_text += f"{i}. {alert}\n"
    
    alert_text += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    alert_text += "🔔 Stay informed and follow local authorities' guidance."
    
    return alert_text


@mcp.tool()
def compare_weather(city1: str, city2: str) -> str:
    """
    Compare current weather between two cities.
    
    Args:
        city1: First city to compare
        city2: Second city to compare
        
    Returns:
        A formatted comparison of weather between the two cities
    """
    # Get weather for both cities (reusing our mock data)
    weather_data = {
        "Tokyo": {"temp": 22, "condition": "Partly Cloudy", "humidity": 65},
        "Paris": {"temp": 18, "condition": "Light Rain", "humidity": 80},
        "New York": {"temp": 25, "condition": "Sunny", "humidity": 55},
        "London": {"temp": 16, "condition": "Overcast", "humidity": 75},
        "Sydney": {"temp": 28, "condition": "Clear", "humidity": 60},
    }
    
    city1_title = city1.title()
    city2_title = city2.title()
    
    weather1 = weather_data.get(city1_title, {"temp": 20, "condition": "Unknown", "humidity": 60})
    weather2 = weather_data.get(city2_title, {"temp": 20, "condition": "Unknown", "humidity": 60})
    
    temp_diff = weather1["temp"] - weather2["temp"]
    humidity_diff = weather1["humidity"] - weather2["humidity"]
    
    comparison = f"🌍 Weather Comparison: {city1_title} vs {city2_title}\n"
    comparison += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    comparison += f"📍 {city1_title:<15} | 📍 {city2_title}\n"
    comparison += f"🌡️  {weather1['temp']}°C{'':<12} | 🌡️  {weather2['temp']}°C\n"
    comparison += f"☁️  {weather1['condition']:<15} | ☁️  {weather2['condition']}\n"
    comparison += f"💧 {weather1['humidity']}% humidity{'':<5} | 💧 {weather2['humidity']}% humidity\n"
    comparison += "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    
    if temp_diff > 0:
        comparison += f"🔥 {city1_title} is {abs(temp_diff)}°C warmer than {city2_title}\n"
    elif temp_diff < 0:
        comparison += f"❄️  {city2_title} is {abs(temp_diff)}°C warmer than {city1_title}\n"
    else:
        comparison += f"🌡️  Both cities have the same temperature\n"
    
    if humidity_diff > 0:
        comparison += f"💧 {city1_title} is {abs(humidity_diff)}% more humid than {city2_title}"
    elif humidity_diff < 0:
        comparison += f"💧 {city2_title} is {abs(humidity_diff)}% more humid than {city1_title}"
    else:
        comparison += f"💧 Both cities have the same humidity level"
    
    return comparison


if __name__ == "__main__":
    # Run the MCP server
    print("🌤️  Starting Weather MCP Server...")
    print("📡 Available tools:")
    print("   • get_current_weather(city)")
    print("   • get_weather_forecast(city, days)")
    print("   • get_weather_alerts(city)")
    print("   • compare_weather(city1, city2)")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    mcp.run() 
import datetime

def calculate_message_type(last_date_str):
    try:
        # Convert Excel string to date object
        deadline = datetime.datetime.strptime(last_date_str, '%Y-%m-%d').date()
        today = datetime.date.today()
        
        diff = (deadline - today).days
        
        # Scenario 1: Exactly 2 days before
        if diff == 2:
            return "Standard Reminder", "The deadline is in 48 hours. Please review."
            
        # Scenario 2: Today is the deadline
        elif diff == 0:
            return "Heads Up", "TODAY is the deadline! Please finalize this now."
            
        # Scenario 3: No immediate action needed
        else:
            return "Status Update", "Everything looks good, keep it up!"
            
    except Exception as e:
        return "Error", f"Could not parse date: {str(e)}"

# Example logic for Zapier output
# result = calculate_message_type(input_data['last_date_str'])

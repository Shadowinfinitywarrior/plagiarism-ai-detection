def calculate_percentage(result, full_text):
    total_lines = full_text.split('\n')
    flagged_lines = result['plagiarized_lines'] if 'plagiarized_lines' in result else result['ai_generated_lines']
    
    percentage = (len(flagged_lines) / len(total_lines)) * 100
    return percentage

def detect_ai_content(text):
    # Load an AI detection model or use a pre-trained API for AI content detection
    # For demo purposes, this will just flag some lines
    ai_lines = ['This line seems AI-generated', 'Another AI-looking line...']
    
    result = {
        'text': text,
        'ai_generated_lines': ai_lines
    }
    return result

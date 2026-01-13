import json
from utils.variables import system_instruction
from utils.gemini import client

def check_spam(submission: dict) -> dict:
    """Main function to check spam"""
    try:
        if not isinstance(submission, dict):
            return {
                "code": 400,
                "message": "Invalid request format"
            }
        
        if not submission:
            return {
                "code": 400,
                "message": "Empty request"
            }
        
        contents = system_instruction + "\n\n" + json.dumps(submission)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents,
            config={"response_mime_type": "text/plain"}  
        )
        
        decision = response.text.strip().lower()
        
        if decision not in ["ok", "spam"]:
            return {
                "code": 500,
                "message": "Unexpected model output"
            }
        
        return {
            "code": 200,
            "message": decision
        }
        
    except Exception as error:
        return {
            "code": 500,
            "message": "Model unavailable"
        }
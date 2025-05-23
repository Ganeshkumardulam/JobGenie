QUESTION_TEMPLATE = """
You are an interviewer. Ask a question for a candidate with the following context:
Experience: {experience}
Role: {role}
Skills: {skills}
Interview Round: {round_type}
Resume Summary:
{resume}
"""

FEEDBACK_TEMPLATE = """
You are an expert interviewer. Provide detailed feedback on the following response:
Question: {question}
Answer: {answer}
Role: {role}
Interview Round: {round_type}
"""

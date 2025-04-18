"""
学校生活与学术讨论
Hi, how’s your school life going? Could you share with me your favorite subject and why?
兴趣爱好与日常生活
Could you describe a typical day in your life? What do you usually do in your free time?
跨文化交流与观点分析
What are some common stereotypes about your country/culture that you would like to dispel?
未来规划与职业发展
Do you have any specific plans for your future, like further studies or internships?
"""
import random


def init_problem(subject):
    if subject == "学校生活与学术讨论":
        return "Hi, how’s your school life going? Could you share with me your favorite subject and why?"

    if subject == "兴趣爱好与日常生活":
        return "Could you describe a typical day in your life? What do you usually do in your free time?"

    if subject == "跨文化交流与观点分析":
        return "What are some common stereotypes about your country/culture that you would like to dispel?"

    if subject == "未来规划与职业发展":
        return "Do you have any specific plans for your future, like further studies or internships?"


def random_problem():
    problems = [
        "Hi, how’s your school life going? Could you share with me your favorite subject and why?",
        "Could you describe a typical day in your life? What do you usually do in your free time?",
        "What are some common stereotypes about your country/culture that you would like to dispel?",
        "Do you have any specific plans for your future, like further studies or internships?"
    ]

    return random.choice(problems)
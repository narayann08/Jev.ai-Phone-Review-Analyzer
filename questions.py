# 14 questions we ask jev for every review
# 7 topic * 2 questions:

from typesafe_sdk import Noul, Score

TOPICS = {
    "Camera": "camera",
    "Battery": "battery",
    "Display": "display",
    "Design": "design",
    "Performance": "performance",
    "Build Quality": "build_quality",
    "Value for Money": "value_for_money",
}

SATISFACTION_LEVELS = [
    "Very dissatisfied",
    "Dissatisfied",
    "Neither satisfied nor dissatisfied, or balanced mixed feedback",
    "Satisfied",
    "Very satisfied",
]

QUESTIONS = {
   #camera
    "camera_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the camera's photos or videos?"
    ),
    "camera_rating": Score(
        instructions="How satisfied is the reviewer with the camera?",
        criteria=SATISFACTION_LEVELS,
    ),

    #battery
    "battery_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about battery life or charging?"
    ),
    "battery_rating": Score(
        instructions="How satisfied is the reviewer with the battery experience?",
        criteria=SATISFACTION_LEVELS,
    ),

    #display
    "display_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the screen?"
    ),
    "display_rating": Score(
        instructions="How satisfied is the reviewer with the display?",
        criteria=SATISFACTION_LEVELS,
    ),

    #design
    "design_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the phone's appearance, shape, or ergonomics?"
    ),
    "design_rating": Score(
        instructions="How satisfied is the reviewer with the design?",
        criteria=SATISFACTION_LEVELS,
    ),

    #performance
    "performance_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about speed, responsiveness, multitasking, or gaming?"
    ),
    "performance_rating": Score(
        instructions="How satisfied is the reviewer with the performance?",
        criteria=SATISFACTION_LEVELS,
    ),

    #build Quality
    "build_quality_mentioned": Noul(
        instructions="Does the reviewer describe an opinion or experience about the phone's materials, sturdiness, or durability?"
    ),
    "build_quality_rating": Score(
        instructions="How satisfied is the reviewer with the build quality?",
        criteria=SATISFACTION_LEVELS,
    ),

    #value for Money
    "value_for_money_mentioned": Noul(
        instructions="Does the reviewer express whether the phone is worth its price?"
    ),
    "value_for_money_rating": Score(
        instructions="How satisfied is the reviewer with the value for money?",
        criteria=SATISFACTION_LEVELS,
    ),
}
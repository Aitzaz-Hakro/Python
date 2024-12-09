from Questions import Questions

question_prompts=[
    "what is color of sky?\na.yellow\nb.white\nc.green\nd.blue",
    "what is color of water?\na.yellow\nb.blue\nc.green\nd.purple",
    "what is color of orange?\na.orange\nb.blue\nc.red\nd.pink"
  ]


questions=[
Questions(question_prompts[0],"d"),
Questions(question_prompts[1],"b"),
Questions(question_prompts[2],"a")
]
def run_test(questions):
  score=0
  for question in questions:
  
    answer=input(question.prompt + "\n")
    if answer==question.answer:
      score+=1
  print("you scored "+ str(score) + "/" + str(len(questions)))

run_test(questions)
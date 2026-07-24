from graph import create_app


app=create_app()

result=app.invoke(
    {
        "user_input":"住宿如何报销",
        "answer":"",
        "intent":""
    }
)

print(result)
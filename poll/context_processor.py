from poll.models import Question

def polls_count(request):
    # Here, objects is a object of model manager
    # Model manager has a default method that is count
    # it will give a count of all the objects available in a question model
    count = Question.objects.count()
    print(" Polls count - " , count)
    # mathi ko fucntion name ra yo same rakhna parni haena hai
    return { "polls_count": count }

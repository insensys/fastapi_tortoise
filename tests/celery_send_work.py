from tests.celery_first_steps import add

result = add.delay(4,5)
timeout = 40
final_result = result.get(timeout)

print (f"Id запроса:{result.id}")
print (f"Сам ответ запроса:{final_result}")
print (f"Задача выполнена успешно: {result.successful()}")
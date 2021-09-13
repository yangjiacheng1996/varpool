from waterpool import Waterpool
from messager import Messager
pool = Waterpool()
pool.add_water("say","Hello world",replace=True)
pool.add_water("repeat","Hello,world!",replace=True)
print(pool)
pool.remove_water("repeat")
pool.remove_water("repeat")

messager = Messager()
messager.post_message("hahaha")
messager.post_message("hahaha")
mes = messager.get_message()
print(mes)


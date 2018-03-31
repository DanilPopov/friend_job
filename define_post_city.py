city_filter = "Москва"  # затем присваивать этой переменной значение из фильтра "Город"
from city_list import all_city_list

print(all_city_list)

# post1 = '''Прямой работодатель #Администратор
# #Работа #Москва Юноши 21+ 50.000 рублей

# Требуется администратор со знанием английского языка в деловое пространство Deworkacy 

# В обязанности входит: 
# • встреча гостей, 
# • содействие в организации мероприятий, 
# • взаимодействие с резидентами пространства, 
# • выполнение поручений, связанных с административно-хозяйственным обеспечением компании (предусмотрены умеренные физические нагрузки). 

# Требования: 
# • молодой человек от 21 года, рост от 180 см, 
# • опыт работы от года 
# • внимательность, 
# • ответственность, 
# • трудолюбие, 
# • открытость миру и людям, 
# • желание развиваться. 
# • гражданство РФ

# Условия: 
# • з/п 50 000р на руки, 
# • официальное оформление 
# • молодой и веселый коллектив, 
# • возможность участвовать в интересных мероприятиях, 
# • график работы: понедельник - пятница с 10:00 до 22:00. 
# • Место работы: ул. Б. Полянка, Corporate Innovations Hub. 

# Резюме с фото и рассказом о себе направлять на i.deworkacy@mail.ru 
# Вконтакте: https://vk.com/irinatotok'''


# def define_city(post_text):
  
#     def get_city_from_post(post_text):
#         # from city_list import all_city_list
#         # print(all_city_list)

#         if city_filter.lower() in post_text:
#             return city_filter
#         else:   
#             for key in all_city_list:
#                 if key in post_text:
#                     return key
    
#     city_in_user_profile = "Санкт-петербург" # затем присваивать этой переменной значение города в контактной информации пользователя ВК, которому принадлежить пост

#     city = get_city_from_post(post_text)
#     if city is None:
#         print(city_in_user_profile)
#         # return city_in_user_profile.lower()
#     else:
#         print(city)
#         # return city


# def define_if_city_equal_filter(city):
#     if city == city_filter.lower():
#         city_equal_filter = True
#     else:
#         city_equal_filter = False
#     print(city_equal_filter)
#     # return city_equal_filter

# define_city(post1)
# define_if_city_equal_filter(post1)
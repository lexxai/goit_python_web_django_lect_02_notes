# PYTHON. DJANGO. LECTION EXAMPLE - NOTES.

## TASK
Проект, що реалізується в цьому розділі, — система управління нотатками на основі фреймворку Django. Користувач може додавати нотатки та описи до них. Додавати будь-яку кількість тегів у нотатці, а, значить, і створювати унікальні для себе теги. Нотатки можуть бути позначені як виконані або можуть бути видалені як не актуальні. Також ми додамо в проект авторизацію та аутентифікацію користувачів, можливість завантажувати аватарку для користувача.

## RESULT

![](doc/signup_01.png)

![](doc/login_01.png)

![](doc/index_01.png)

![](doc/tag_01.png)

![](doc/tag_02.png)

![](doc/note_01.png)

![](doc/index_02.png)

![](doc/note_02.png)

![](doc/detail_01.png)

![](doc/index_03.png)

![](doc/detail_02.png)

### PROFILES

![](doc/profile_01.png)

![](doc/profile_02.png)

![](doc/profile_03.png)

### DELETE USER AND AVATAR PROFILE

![](doc/delete_user.png)

![](doc/delete_user_form.png)

![](doc/profile_avatar_t9.png)

![](doc/user_was_deleted.png)

![](doc/profile_avatar_t9-deleted.png)





### DOCKER

```
scipts/docker_build_docker-compose.cmd
[+] Building 28.8s (13/13) FINISHED                                                                                  docker:default
 => [code internal] load build definition from Dockerfile                                                                      0.1s
 => => transferring dockerfile: 1.11kB                                                                                         0.0s 
 => [code internal] load .dockerignore                                                                                         0.1s 
 => => transferring context: 154B                                                                                              0.0s 
 => [code internal] load metadata for docker.io/library/python:3.11                                                            2.7s 
 => [code auth] library/python:pull token for registry-1.docker.io                                                             0.0s
 => [code 1/7] FROM docker.io/library/python:3.11@sha256:652c9f890a7f38bab4d67ee95c54d72955792623122cfea0a87aa74d927e41ae      0.1s
 => => resolve docker.io/library/python:3.11@sha256:652c9f890a7f38bab4d67ee95c54d72955792623122cfea0a87aa74d927e41ae           0.1s 
 => [code internal] load build context                                                                                         0.1s
 => => transferring context: 5.15kB                                                                                            0.0s
 => CACHED [code 2/7] WORKDIR /app                                                                                             0.0s
 => [code 3/7] COPY . .                                                                                                        0.1s
 => [code 4/7] COPY run.sh run.sh                                                                                              0.1s
 => [code 5/7] COPY notes/ notes/                                                                                              0.1s
 => [code 6/7] COPY requirements.txt requirements.txt                                                                          0.1s
 => [code 7/7] RUN pip install -r requirements.txt                                                                            23.9s
 => [code] exporting to image                                                                                                  1.3s
 => => exporting layers                                                                                                        1.3s
 => => writing image sha256:e019f6cb476c7abd1394edd3c3ad106d29bb0b9aa45ab04ba521db24c4e38806                                   0.0s
 => => naming to docker.io/library/lect_10_02_notes-code                                                                       0.0s
[+] Running 2/2
 ✔ Container lect_10_02_notes-pg-1    Running                                                                                  0.0s
 ✔ Container lect_10_02_notes-code-1  Started                                                                                 14.3s
 ```

![](doc/docker_01.png)


![](doc/docker_02.png)



### ADDON

Насправді наш застосунок можна трохи покращити. Як самостійне завдання ми рекомендуємо вам дописати наступний функціонал:

1. Зробіть можливість видаляти і виконані завдання (зараз застосунок видаляє тільки невиконані нотатки).
2. Реалізуйте можливість, окрім виведення на головній сторінці всіх нотаток, виведення лише завершених або незавершених нотаток на вибір.
3. Реалізуйте можливість редагування та видалення тегів та окремий перегляд усіх своїх тегів.
4. Реалізуйте можливість редагування незавершених нотаток
5. Pagination


#### ADDON SOLUTION 1.

 ![before_addon_1](doc/addon_1_before.png)

 ![after_addon_1](doc/addon_1_after.png)

 ![after_del_addon_1](doc/addon_1_after_del.png)


#### ADDON SOLUTION 2.

![addon_2_all](doc/addon_2_all.png)

![addon_2_done](doc/addon_2_done.png)

![addon_2_not_done](doc/addon_2_not_done.png)

#### ADDON SOLUTION 3.

![addon_3_list](doc/addon_3_list.png)

![addon_3_edit](doc/addon_3_edit.png)

![addon_3_filter_tag](doc/addon_3_filter_tag.png)

![addon_3_edit_note_tag](doc/addon_3_edit_note_tag.png)

#### ADDON SOLUTION 4.



#### ADDON SOLUTION 5.
![addon_5_page](doc/addon_5_pagination.png)
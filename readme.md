Київське метро складається з 54 станцій
Київське метро має 56 прокладених зєднань


Маршрути складені для аналізу методами BFS і DFS ідентичні до першої пересадки. Один з маршуртів продовжую шлях по гілці, другий пересаджується при першій же можливості
| dfs_result                     | bfs_result                     |
---------------------------------------------------------------
| Akademmistechko                | Akademmistechko                |
| Zhytomyrska                    | Zhytomyrska                    |
| Sviatoshyn                     | Sviatoshyn                     |
| Nyvky                          | Nyvky                          |
| Beresteiska                    | Beresteiska                    |
| Shuliavska                     | Shuliavska                     |
| Politekhnichnyi Instytut       | Politekhnichnyi Instytut       |
| Vokzalna                       | Vokzalna                       |
| Universytet                    | Zoloti Vorota                  |
| Teatralna                      | Lvivska Brama                  |
| Khreshchatyk                   | Universytet                    |
| Arsenalna                      | Teatralna                      |
| Zviretska                      | Palac Sportu                   |
| Hydropark                      | Lukianivska                    |
| Livoberezhna                   | Khreshchatyk                   |
| Darnytsia                      | Klovska                        |
| Chernihivska                   | Ploshcha UA Hero               |
| Lisova                         | Dorohozhychi                   |
| Maidan Nezalezhnosti           | Arsenalna                      |
| Poshtova Ploshcha              | Maidan Nezalezhnosti           |
| Kontraktova Ploshcha           | Pecherska                      |
| Tarasa Shevchenka              | Olimpiiska                     |
| Pochaina                       | Vidubichi                      |
| Petrovka                       | Syrets                         |
| Obolon                         | Zviretska                      |
| Warshavska                     | Poshtova Ploshcha              |
| Heroiv Dnipra                  | Palats Ukraina                 |
| Ploshcha UA Hero               | Teluchka                       |
| Olimpiiska                     | Hydropark                      |
| Palats Ukraina                 | Kontraktova Ploshcha           |
| Lubitska                       | Lubitska                       |
| Demiivska                      | Slavytuck                      |
| holosiivska                    | Livoberezhna                   |
| Vasilkivska                    | Tarasa Shevchenka              |
| Vistavkoviu Center             | Demiivska                      |
| Ipodrom                        | Osokorky                       |
| Teremky                        | Darnytsia                      |
| Pecherska                      | Pochaina                       |
| Klovska                        | holosiivska                    |
| Palac Sportu                   | Pozniyaki                      |
| Zoloti Vorota                  | Chernihivska                   |
| Vidubichi                      | Petrovka                       |
| Teluchka                       | Vasilkivska                    |
| Slavytuck                      | Kharkivska                     |
| Osokorky                       | Lisova                         |
| Pozniyaki                      | Obolon                         |
| Kharkivska                     | Vistavkoviu Center             |
| Vurlucia                       | Vurlucia                       |
| Borispilska                    | Warshavska                     |
| Chervonuy hutir                | Ipodrom                        |
| Lvivska Brama                  | Borispilska                    |
| Lukianivska                    | Heroiv Dnipra                  |
| Dorohozhychi                   | Teremky                        |
| Syrets                         | Chervonuy hutir                |


Обравши місце відправлення ми можемо за допомогою метода Дейсктри отримати відомості, за який проміжок часу зможем добратись до будь-якої станції
-----------------------------------------------------
| Station                        | Travel time (min)    |
-----------------------------------------------------
| Akademmistechko                | 0                    |
| Zhytomyrska                    | 3                    |
| Sviatoshyn                     | 6                    |
| Nyvky                          | 9                    |
| Beresteiska                    | 12                   |
| Shuliavska                     | 15                   |
| Politekhnichnyi Instytut       | 18                   |
| Vokzalna                       | 21                   |
| Universytet                    | 24                   |
| Teatralna                      | 27                   |
| Khreshchatyk                   | 30                   |
| Arsenalna                      | 33                   |
| Zviretska                      | 36                   |
| Hydropark                      | 39                   |
| Livoberezhna                   | 42                   |
| Darnytsia                      | 45                   |
| Chernihivska                   | 48                   |
| Lisova                         | 51                   |
| Heroiv Dnipra                  | 59                   |
| Warshavska                     | 56                   |
| Obolon                         | 53                   |
| Petrovka                       | 50                   |
| Pochaina                       | 47                   |
| Tarasa Shevchenka              | 44                   |
| Kontraktova Ploshcha           | 41                   |
| Poshtova Ploshcha              | 38                   |
| Maidan Nezalezhnosti           | 35                   |
| Ploshcha UA Hero               | 32                   |
| Olimpiiska                     | 35                   |
| Palats Ukraina                 | 38                   |
| Lubitska                       | 41                   |
| Demiivska                      | 44                   |
| holosiivska                    | 47                   |
| Vasilkivska                    | 50                   |
| Vistavkoviu Center             | 53                   |
| Ipodrom                        | 56                   |
| Teremky                        | 59                   |
| Syrets                         | 33                   |
| Dorohozhychi                   | 30                   |
| Lukianivska                    | 27                   |
| Lvivska Brama                  | 24                   |
| Zoloti Vorota                  | 24                   |
| Palac Sportu                   | 27                   |
| Klovska                        | 30                   |
| Pecherska                      | 33                   |
| Vidubichi                      | 35                   |
| Teluchka                       | 38                   |
| Slavytuck                      | 41                   |
| Osokorky                       | 44                   |
| Pozniyaki                      | 47                   |
| Kharkivska                     | 50                   |
| Vurlucia                       | 53                   |
| Borispilska                    | 56                   |
| Chervonuy hutir                | 59                   |
-----------------------------------------------------
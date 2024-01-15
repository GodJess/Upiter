var users = {{ ussers | safe }};
        document.addEventListener('DOMContentLoaded', function() {
// Функция для отображения пользователей
            function displayUsers(users) {
                console.log('Received users:', users);  
                var container = document.getElementById('users');
                container.innerHTML = '';  
                for(var i = 0; i < Math.min(6,users.length); i++) {  
                    var user = users[i];
                    console.log('Displaying user:', user);
                    var userDiv = document.createElement('div');  
                    userDiv.className = 'people';
                    userDiv.innerHTML = 
                        '<div class="pip">' +
                            '<form action="" method="post">' +
                                '<input type="hidden" name="csrfmiddlewaretoken" value="hQZSTf55qK00xUUTpmUEefrMq2PAqb7rcUmpUNPqt8ZggCJ49KQVpczsENoxWaUX">' +
                                '<input type="hidden" name="name" value="' + user.name + '">' +
                                '<input type="hidden" name="surname" value="' + user.surname + '">' +
                                '<input type="hidden" name="phone" value="' + user.phone + '">' +
                                '<div class="block_photo">' +
                                    '<button class="buttt" type="submit"><img class="peopimg" src="' + user.photo + '" alt=""></button>' +
                                '</div>' +
                            '</form>' +
                            '<p class="people_name">' + user.name + '</p>' +
                        '</div>';
                    container.appendChild(userDiv);
                }
            }

            
            displayUsers(users);

            // Обработка поискового запроса
            document.getElementById('search').addEventListener("change", function(event) {
                event.preventDefault();
                var searchInput = document.getElementById('search-input').value;
                
            });
        });
function load_comments() {
    $.get( `get_comments/` )
        .done(function( comments ) {
            $.each(comments, (i, comment)=>{
                $('#comments').append(`<tr>
                            <td>${comment['id']}</td>
                            <td>${comment['Surname']}</td>
                            <td>${comment["Name"]}</td>
                            <td>${comment['Patronymic'] || ""}</td>
                            <td>${comment['Region'] || ""}</td>
                            <td>${comment['City'] || ""}</td>
                            <td>${comment['Phone'] || ""}</td>
                            <td>${comment['E-mail'] || ""}</td>
                            <td class="comment_field">${comment['Comment']}</td>
                            <td><button onclick="delete_row(${comment['id']})" id="button" value="${comment['id']}">Удалить</button></td>
                        </tr>`)
            })
        });
}

load_comments()

function delete_row(id) {
    $.get(`delete_row/${id}`)
        .done()
    {
        $('#comments').html(`<table id="comments">
            <tr>
                <th>ID комментария</th>
                <th>Фамилия</th>
                <th>Имя</th>
                <th>Отчество</th>
                <th>Регион</th>
                <th>Город</th>
                <th>Контактный телефон</th>
                <th>E-mail</th>
                <th>Комментарий</th>
                <th>Удалить</th>
            </tr>`)
        load_comments()
    }
}

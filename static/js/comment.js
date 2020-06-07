


const load_cities = (city_id) => {
  $.get( `get_city_by_region_id/${city_id}` )
      .done(function( cities ) {
        // получаем ассоцифтивный массив с городами

        // обнуляем селект, чтобы не накапливаличь города при мзменении региона
        $('#city').html(`<option value="">Выберите город</option>`)

        $.each(cities,function(i, value){
          // для каждого элемента получаем ключ, значение и вставляем в элементы селекта
          $('#city').append(`<option value="${i}">${value}</option>`)
        });
      });
}


$(document).ready(function() {
  fetch_data();
  function fetch_data() {
    $.ajax({
      url: 'region',
      method: "GET",
      dataType: 'json',
      success: function(data) {
      }
    });

  }

  var validSurname = false;
  var validName = false;
  var validPhone = true;
  var validEmail = true;
  var validComment = false;
  $("#phone").inputmask("+7(999)9999999")

  $('#form').submit(function(e) {
    e.preventDefault();
    var surname = $('#surname').val();
    var name = $('#name').val();
    var phone = $('#phone').val();
    var email = $('#e-mail').val();

    var comment = $('#comment').val();

    $(".error").remove();
    if (surname.length< 1) {
      $('#surname').addClass('empty_field');
      validSurname = false;
    } else {
      validSurname = true;
      $('#surname').removeClass('empty_field');
    }

    if (name.length< 1) {
      $('#name').addClass('empty_field');
      validName = false;
    } else {
      validName = true;
      $('#name').removeClass('empty_field');
    }

    if (phone.length > 1){
      var regEx = /^\+[0-9]{1}\([0-9]{3}\)+[0-9]{7}$/i;
      var validphone = regEx.test(phone);
      if (!validphone) {
        $('#phone').addClass('empty_field');
        validPhone = false;
      } else {
        validPhone = true;
        $('#phone').removeClass('empty_field');
      }
    }

    if (email.length > 1) {
      var regEx = /^[a-z0-9_-]+@[a-z0-9-]+\.[a-z]{2,6}$/i ;
      var validemail = regEx.test(email);
      if (!validemail) {
        $('#e-mail').addClass('empty_field');
        validEmail = false;
      } else {
        validEmail = true;
        $('#e-mail').removeClass('empty_field');
      }
    }
    if (comment.length< 1) {
      $('#comment').addClass('empty_field');
      validComment = false;
    } else {
      validComment = true;
      $('#comment').removeClass('empty_field');
    }

    if(validSurname == true && validName == true && validEmail == true && validPhone == true && validComment == true) {
        $("form").unbind('submit').submit();
      }
  });
});

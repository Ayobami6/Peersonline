// TODO: fix the like pluralize
$(document).ready(function () {
  var csrftoken = getCookie("csrftoken");

  $(document).on("click", "div#like", function () {
    var likeButton = $(this).find("#like-button");
    var post_id = likeButton.attr("data-pk");
    var href = likeButton.attr("data-href");
    var like_count = $(this).find("#like-count");

    $.ajax({
      url: href,
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      data: {
        post_id: post_id,
      },
      success: function (response) {
        console.log(response.total_likes);
        like_count.text(response.total_likes);
        if (response.total_likes != 1) {
          $(this).text("Likes");
        } else {
          $(this).text("Like");
        }
      },
    });
  });
  $("form#search-form").on("submit", function (e) {
    e.preventDefault();
    var query = $("input#search-input").val();
    var searchButton = $(this).find("#search-button");
    $.ajax({
      url: `posts/search`,
      type: "GET",
      headers: { "X-CSRFToken": csrftoken },
      data: {
        query: query,
      },
      success: function (response) {
        console.log(response.posts);
        for (var i = 0; i < response.posts.length; i++) {
          var post = response.posts[i];
          console.log(post.id);
          console.log(post.title);
          console.log(post.content);
          console.log(post.author);
          console.log(post.created_at);
          console.log(post.likes);
        }
      },
    });
  });

  $("#form-button").click(function () {
    $("#session-form").submit(function (e) {
      e.preventDefault();
      var formData = $(this).serialize();
      var api_endpoint = "api/mentor_sessions/";
      $.ajax({
        url: api_endpoint,
        type: "POST",
        data: formData,
        success: function (response) {
          $("#alert-placeholder").html(`<div
          class="alert alert-success d-flex align-items-center"
          role="alert">
          <svg
            class="bi flex-shrink-0 me-2"
            width="24"
            height="24"
            role="img"
            aria-label="Success:">
            <use xlink:href="#check-circle-fill" />
          </svg>
          <div>Sucess! Thanks for reqistering to mentor peers</div>
        </div>`);
        },
        error: function (error) {
          console.log(formData);
          $("#alert-placeholder").html(`
          <div class="alert alert-danger d-flex align-items-center" role="alert">
          <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
          <div>
          Failed to register to mentor peers. Please try again.
          </div>
          </div>
          `);
        },
      });
    });
  });
  function loadLatestSession() {
    $.ajax({
      url: "api/mentor_sessions/",
      type: "GET",
      success: function (response) {
        response.sort((a, b) => {
          return new Date(b.created_at) - new Date(a.created_at);
        });
        var latest_session = response[0];
        console.log(latest_session);
        $("#feat-session").html(
          `<div class="card" style="width: 20rem;">
          <img src="..." class="card-img-top" alt="...">
          <div class="card-body">
              <p class="card-text">${latest_session.topic_title}.</p>
          </div>
      </div>`
        );
      },
    });
  }
  loadLatestSession();
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

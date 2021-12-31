$(document).ready(function(){
    $("li").removeClass("active");
    var all_lists = $("li");
    var pathname = window.location.pathname; // Get pathname from url

    $.each(all_lists, function (index, child) {
            if (pathname == "/") {
                if (child.textContent === "Social/Text") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/image/") {
              if (child.textContent === "Image") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/music/") {
              if (child.textContent === "Music/Audio") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/video/") {
              if (child.textContent === "Video") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/version/") {
              if (child.textContent === "Version Control") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/finance/") {
              if (child.textContent === "Finance") {
                    $(child).addClass("active");
                }
            }

            else if (pathname == "/visual/") {
              if (child.textContent === "Visual") {
                    $(child).addClass("active");
                }
            }
    });
});

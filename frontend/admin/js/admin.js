$(document).ready(function () {

    /* ===== LOAD SHOWTIMES ===== */
    if ($("#showtimeTable").length) {
        $.get("http://127.0.0.1:5000/api/showtimes", function (data) {
            let html = "";
            data.forEach(s => {
                html += `
                    <tr>
                        <td>${s.show_date}</td>
                        <td>${s.show_time}</td>
                        <td>${s.movie_id}</td>
                    </tr>
                `;
            });
            $("#showtimeTable").html(html);
        });
    }

});

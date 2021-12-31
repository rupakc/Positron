function plot_wordcloud(divElementId,responseJson) {
    Highcharts.chart(divElementId, {
        series: [{
            type: 'wordcloud',
            data: responseJson['data'],
            name: 'Frequency'
        }],
        title: {
            text: responseJson['title_text']
        }
    });
}

function plot_highchart(divIdElement,responseJson) {

    Highcharts.chart(divIdElement, {
                legend: {
                    enabled: false
                },
                chart: {
                    type: 'column'
                },
                title: {
                    text: responseJson['title_text']
                },
                subtitle: {
                    text: responseJson['subtitle_text']
                },
                xAxis: {
                    categories:responseJson['category_list'],
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Percentage'
                    }
                },
                tooltip: {
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        pointPadding: 0.2,
                        borderWidth: 0
                    }
                },
                series: responseJson['series_data_list']
            });
    }

function getErrorMessage(jqXHR, exception) {
    var msg = '';
    if (jqXHR.status === 0) {
        msg = 'Not connect.\n Verify Network.';
    } else if (jqXHR.status == 404) {
        msg = 'Requested page not found. [404]';
    } else if (jqXHR.status == 500) {
        msg = 'Internal Server Error [500].';
    } else if (exception === 'parsererror') {
        msg = 'Requested JSON parse failed.';
    } else if (exception === 'timeout') {
        msg = 'Time out error.';
    } else if (exception === 'abort') {
        msg = 'Ajax request aborted.';
    } else {
        msg = 'Uncaught Error.\n' + jqXHR.responseText;
    }
    alert(msg)
}

$(document).ready(function() {
     var input = document.getElementById("search_term");
     input.addEventListener("keyup", function(event) {
     event.preventDefault();
        if (event.keyCode === 13) {
            document.getElementsByClassName("btn-success")[0].click();
        }
     });
     $('.btn-success').click(function() {
         var pathname = window.location.pathname;
         if (pathname == "/visual/") {
            search_term = $('#search_term').val();
            data_sources = $('#online_data_sources').val();
            database_sources = $('#database_dropdown').val();
          $("div#divLoading").addClass('show');
          $("div#divLoading").show();
          $.ajax({
            type: "GET",
            url: "/visualprocessor",
            data: {'search':search_term,'data_sources':data_sources,'database_sources':database_sources},
            success: function(data){
                $('#submit_button').nextAll().empty().removeClass();
                $.each(data['data_sources'],function(index,data_source) {
                    var data_type_response = data[data_source]
                    var response_list = data_type_response['response_list']
                    $.each(response_list,function(inner_index,response_operation) {
                        $('#submit_button').after("<div id=" + response_operation + " class='col col-md-4 thumbnail'>  </div>")
                        if (response_operation == 'wordcloud') {
                            plot_wordcloud(response_operation,data_type_response[response_operation]);
                        } else {
                            plot_highchart(response_operation, data_type_response[response_operation]);
                        }
                    });
                });
                $('#submit_button').after("<br/>")
                $('div#divLoading').removeClass('show');
                $('div#divLoading').hide();
            },
            error: function (jqXHR, exception) {
                $('div#divLoading').removeClass('show');
                $('div#divLoading').hide();
                getErrorMessage(jqXHR, exception);
            }
          });
         }
     });
});

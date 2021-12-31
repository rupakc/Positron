$(document).ready(function() {
    var emotionColorCodes = {
                            'Neutral' : "#f2f2a6",
                            'Negative':"#ef868b",
                            'Positive':"#a1eaaa"
                            }
	var allCells = $(".dataframe td");
        $.each(allCells, function (index, child) {
             if(emotionColorCodes.hasOwnProperty(child.textContent)){
                $(child).css("background-color", emotionColorCodes[child.textContent]);
              }
        });
    });
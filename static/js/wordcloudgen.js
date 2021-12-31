function wordFreq(string) {
	return string.replace(/[.]/g, '')
  	.split(/\s/)
    .reduce((map, word) =>
    	Object.assign(map, {
      	[word]: (map[word])
        	? map[word] + 1
          : 1,
      }),
    	{}
    );
}


$(document).ready(function() {
    var textContentElements = $(".lead")
    var pathname = window.location.pathname;
    if (pathname == "/") {
        $.each(textContentElements,function(index,elementContent) {
            var textValue = elementContent.textContent
            textValue = textValue.removeStopWords();
            var textWeight = []
            var wordFreqMap = wordFreq(textValue)
            Object.keys(wordFreqMap).forEach(function(word) {
                textWeight.push({'text':word,'weight':wordFreqMap[word]})
            });
            $(elementContent).after("<div id=" + index.toString() +  " style='margin-left:200px' >  </div>")
            var elementId = "#" + index.toString()
            $(elementId).jQCloud(textWeight, {
                autoResize: true,
                width: 700,
                height: 700
            });
            $(elementId).show()
        });
    }
});


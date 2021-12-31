$(document).ready(function() {
    toastr.options.timeOut = 1500; // 1.5s
    toastr.info('Page Loaded!');
    $('.dataframe').load(function() {
       toastr.success('Data Retrieved');
    });
 });
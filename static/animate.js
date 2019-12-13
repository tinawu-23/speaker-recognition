$(document).ready(function () {
    $('#chooseFile1').bind('change', function () {
        var filename = $("#chooseFile1").val();
        if (/^\s*$/.test(filename)) {
            $(".file-upload1").removeClass('active');
            $("#noFile1").text("No file chosen...");
        }
        else {
            $(".file-upload1").addClass('active');

            let file = document.getElementById("chooseFile1").files[0];  // file from input
            let req = new XMLHttpRequest();
            let formData = new FormData();

            formData.append("file", file);
            req.open("POST", '/');
            req.send(formData);

            $("#noFile1").text(filename.replace("C:\\fakepath\\", ""));
        }
    });
    $('#chooseFile2').bind('change', function () {
        var filename = $("#chooseFile2").val();
        if (/^\s*$/.test(filename)) {
            $(".file-upload2").removeClass('active');
            $("#noFile2").text("No file chosen...");
        }
        else {
            $(".file-upload2").addClass('active');
            let file = document.getElementById("chooseFile2").files[0];  // file from input
            let req = new XMLHttpRequest();
            let formData = new FormData();

            formData.append("file", file);
            req.open("POST", '/');
            req.send(formData);

            $("#noFile2").text(filename.replace("C:\\fakepath\\", ""));
        }
    });
    $('#chooseFile3').bind('change', function () {
        var filename = $("#chooseFile3").val();
        if (/^\s*$/.test(filename)) {
            $(".file-upload3").removeClass('active');
            $("#noFile3").text("No file chosen...");
        }
        else {
            $(".file-upload3").addClass('active');
            let file = document.getElementById("chooseFile3").files[0];  // file from input
            let req = new XMLHttpRequest();
            let formData = new FormData();

            formData.append("file", file);
            req.open("POST", '/');
            req.send(formData);

            $("#noFile3").text(filename.replace("C:\\fakepath\\", ""));
        }
    });
    $('#chooseFile4').bind('change', function () {
        var filename = $("#chooseFile4").val();
        if (/^\s*$/.test(filename)) {
            $(".file-upload4").removeClass('active');
            $("#noFile4").text("No file chosen...");
        }
        else {
            $(".file-upload4").addClass('active');
            let file = document.getElementById("chooseFile4").files[0];  // file from input
            let req = new XMLHttpRequest();
            let formData = new FormData();

            formData.append("file", file);
            req.open("POST", '/');
            req.send(formData);

            $("#noFile4").text(filename.replace("C:\\fakepath\\", ""));
        }
    });
});
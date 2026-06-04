$(function(){

    let result = $("#quiz-result").data("result");

    console.log("result=", result);

    if(result === "Correct!"){

        $("#result-title").text("🎉 正解！");

        $("#wrong-buttons").hide();

        $("#result-modal").fadeIn();

    }

    else if(result === "wow,Wrong!"){

        $("#result-title").text("❌ 不正解");

        $("#correct-buttons").hide();

        $("#result-modal").fadeIn();

    }

});

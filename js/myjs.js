$(function(){
  $("i.icon").addClass('fa-3x');
  $("div.class-body").addClass('text-justify');
  $('div.hreview').addClass('col-md-3');
  $('div.hreview').addClass('col-sm-4');
  $('div.hreview').addClass('col-xs-6');
  $('img').addClass('img-responsive');
  $('div.row div.col-md-3').addClass('thumbnail');
});
window.onload = function(){
  // var array = new Array();
  // array[0]="./images/images.jpg";
  // array[1]="./images/poster-1.jpg";
  // array[2]="./images/poster-2.jpg";
  // array[3]="./images/poster-3.jpg";
  // array[4]="./images/poster-4.jpg";
  // array[5]="./images/poster-5.jpg";
  // array[6]="./images/poster-6.jpg";
  // array[7]="./images/poster-7.jpg";
  // array[8]="./images/poster-8.jpg";
  // array[9]="./images/poster-9.jpg";
  // array[10]="./images/poster-10.jpg";
  // array[11]="./images/poster-11.jpg";
  // array[12]="./images/poster-12.jpg";
  // array[13]="./images/poster-13.jpg";
  // array[14]="./images/poster-14.jpg";
  // array[15]="./images/poster-15.jpg";

  // console.log(array);
  // for(var i = 0;i<array.length;i++){
    // console.log(array[i]);
  // var div = document.createElement("div");
  // var div = $("<div></div>")
  // var img = document.createElement("img");
  // var img = $("<img>");

  // img.src = array[i];
  // img.attr("src",array[i]);
  // div.addClass("hreview thumbnail yinying col-md-3 col-sm-4 col-xs-6");
  // img.addClass("img-responsive");
  // img.appendto(div);
  // console.log(div[0]);
  // console.log(img[0]);
  // div.append(img);
  // $(".review").append(div);
};
window.onload = function(){
  // masonry.desandro.com
    $('div.review').masonry({
      itemSelector: '.hreview'
    });
  };
};

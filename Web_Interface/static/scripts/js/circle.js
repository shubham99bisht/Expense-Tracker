

//	create by nasir farhadi
//	email : nasirfarhadi92@gmail.com
//	Github : nasirfarhadi92



	let i=2;

	function getDotCircleInterval(){
	    if(screen){
	        if(screen.width>600){
	            return 5000;
	        }
	    }
	    return 3000;
	}

	function getFeaturesImgSrc(id, is_white){
	    var src = "";
	    switch(id) {
          case 1:
            src = is_white ? "./static/images/features/2d 3d white.svg" : "./static/images/features/2d 3d.svg";
            break;
          case 2:
            src = is_white ? "./static/images/features/resolution white.svg" : "./static/images/features/resolution.svg";
            break;
          case 3:
            src = is_white ? "./static/images/features/mix n match white.svg" : "./static/images/features/mix n match.svg";
            break;
          case 4:
            src = is_white ? "./static/images/features/ar lips white.svg" : "./static/images/features/ar lips.svg";
            break;
          case 5:
            src = is_white ? "./static/images/features/model faces white.svg" : "./static/images/features/model faces.svg";
            break;
          case 6:
            src = is_white ? "./static/images/features/trak white.svg" : "./static/images/features/trak.svg";
            break;
        }
        return src;
	}


	$(document).ready(function(){
		var radius = 200;
		var fields = $('.itemDot');
		var container = $('.dotCircle');
		var width = container.width();
        radius = width/2.5;

		var height = container.height();
		var angle = 0, step = (2*Math.PI) / fields.length;
		fields.each(function() {
			var x = Math.round(width/2 + radius * Math.cos(angle) - $(this).width()/2);
			var y = Math.round(height/2 + radius * Math.sin(angle) - $(this).height()/2);

			$(this).css({
				left: x + 'px',
				top: y + 'px'
			});
			angle += step;
		});


		$('.itemDot').click(function(){

			var dataTab= $(this).data("tab");
			$('.itemDot').removeClass('active');
			$(this).addClass('active');
			$('.CirItem').removeClass('active');
			$( '.CirItem'+ dataTab).addClass('active');
			i=dataTab;
			$('#features-banner').attr("src","./static/images/features/"+i+".png");

			$('.dotCircle').css({
				"transform":"rotate("+(360-(i-1)*36)+"deg)",
				"transition":"2s"
			});
			$('.itemDot').css({
				"transform":"rotate("+((i-1)*36)+"deg)",
				"transition":"1s"
			});
			for (j = 1; j < 7; j++) {
			    $('#features_img'+j).attr("src",getFeaturesImgSrc(parseInt(j), false));
			}
			$('#features_img'+i).attr("src",getFeaturesImgSrc(parseInt(i), true));
		});

		$('.features_img').hover(function(){
		        var i = parseInt($(this).attr('id').replace("features_img",""));
                $(this).attr("src",getFeaturesImgSrc(i, true));
            }, function(){
                var i = parseInt($(this).attr('id').replace("features_img",""));
                if(!$('.CirItem'+i).attr('class').includes("active")){
                    $(this).attr("src",getFeaturesImgSrc(i, false));
                }
        });

		setInterval(function(){
			var dataTab= $('.itemDot.active').data("tab");
			if(dataTab>6||i>6){
                dataTab=1;
                i=1;
			}
			$('.itemDot').removeClass('active');
			$('[data-tab="'+i+'"]').addClass('active');
			$('.CirItem').removeClass('active');
			$( '.CirItem'+i).addClass('active');
			$('#features-banner').attr("src","./static/images/features/"+i+".png");

			$('#features_img'+i).attr("src",getFeaturesImgSrc(parseInt(i), true));
			j = parseInt(i)==1?6:parseInt(i)-1
			$('#features_img'+j).attr("src",getFeaturesImgSrc(j, false));

			i++;


			$('.dotCircle').css({
				"transform":"rotate("+(360-(i-2)*36)+"deg)",
				"transition":"2s"
			});
			$('.itemDot').css({
				"transform":"rotate("+((i-2)*36)+"deg)",
				"transition":"1s"
			});

			}, getDotCircleInterval());

	});

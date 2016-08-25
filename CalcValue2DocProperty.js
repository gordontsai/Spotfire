test=function()
{

//The first id is the id of the calculated value. IMPORTANT: Make sure to include the "#" sign before the id when creating the var
//The second id is the id of the document property. 
//For this reason you have to create the document property as an input field in the actual text area
//for this to work. This is because it can't be hidden if you are to use the elem.focus() function below.

var CumOilThruDaysFlat =$("#cb35e60c815048318a1ad95e13e5eee4").text();
elem = document.getElementById("2e4b5f0cbc234523b9a3a5a887f490ba")
elem.value = CumOilThruDaysFlat;
elem.focus();

var Cum2Date =$("#74e24bf2565942d68811ebb0b4062415").text();
elem = document.getElementById("52441db136254fb59ca122c28ca9aba1")
elem.value = Cum2Date;
elem.focus();

var MonthsProduced =$("#159a8e1e252f4aa0ae7fce25764d2256").text();
elem = document.getElementById("a574e2474b254b00ba97e571f4873dad")
elem.value = MonthsProduced;
elem.focus();

var CommercialEUR =$("#a5833c25f11049b5844448fd797db831").text();
elem = document.getElementById("9ceb12b1113347e6ab2969583209e28e")
elem.value = CommercialEUR;
elem.focus();







}
setInterval(test,1);

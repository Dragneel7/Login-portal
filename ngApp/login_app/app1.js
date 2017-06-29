angular.module('ngSnake', [])

  .controller('snakeCtrl', function($scope,$http) {
    var BOARD_SIZE = 18;

      $scope.score_player1=0;
      $scope.score_player2=0;

    window.onbeforeunload = function() {
  return "Data will be lost if you leave the page, are you sure?";
};

    $scope.value=function(col,row){
      if($scope.board[col][row]==='a'){
        return 'a';
      }
       else if($scope.board[col][row]==='b'){
        return 'b';
      }
      else if($scope.board[col][row]==='c'){
        return 'c';
      }
      else if($scope.board[col][row]==='d'){
        return 'd';
      }
      else if($scope.board[col][row]==='e'){
        return 'e';
      }
      else if($scope.board[col][row]==='f'){
        return 'f';
      }
      else if($scope.board[col][row]==='g'){
        return 'g';
      }
      else if($scope.board[col][row]==='h'){
        return 'h';
      }
      else if($scope.board[col][row]==='i'){
        return 'i';
      }
      else if($scope.board[col][row]==='j'){
        return 'j';
      }
      else if($scope.board[col][row]==='k'){
        return 'k';
      }
      else if($scope.board[col][row]==='l'){
        return 'l';
      }
      else if($scope.board[col][row]==='m'){
        return 'm';
      }
      else if($scope.board[col][row]==='n'){
        return 'n';
      }
      else if($scope.board[col][row]==='o'){
        return 'o';
      }
      else if($scope.board[col][row]==='p'){
        return 'p';
      }
      else if($scope.board[col][row]==='q'){
        return 'q';
      }
      else if($scope.board[col][row]==='r'){
        return 'r';
      }
      else if($scope.board[col][row]==='s'){
        return 's';
      }
      else if($scope.board[col][row]==='t'){
        return 't';
      }
      else if($scope.board[col][row]==='u'){
        return 'u';
      }
      else if($scope.board[col][row]==='v'){
        return 'v';
      }
      else if($scope.board[col][row]==='w'){
        return 'w';
      }
      else if($scope.board[col][row]==='x'){
        return 'x';
      }
      else if($scope.board[col][row]==='y'){
        return 'y';
      }
      else if($scope.board[col][row]==='z'){
        return 'z';
      }
      else if($scope.board[col][row]===""){
           $scope.board[col][row]=false;
      if($scope.player===Player2){
      $scope.score_player1=$scope.score_player1-10;
        }
      else if($scope.player===Player1){
          $scope.score_player2=$scope.score_player2-10;
      }
      }
       else{
        $scope.board[col][row]=false;

      }
    }

    var Player1=1,Player2=2;
    $scope.player=Player1;
    

    
     $scope.setStyling = function(col, row,player) {
      if($scope.board[col][row] === false){
      return 'lightgrey';
    }
    if($scope.board[col][row] != false && player === Player1){
      return '#d580ff';
    }
     if($scope.board[col][row] != false){
      return '#8080ff';
    }
    

    };

        


    $scope.make_active = function(col,row){
     
      $scope.board[col][row]=prompt("enter a letter");
      
      var word_vertical =[];
      var a=0;
      var b=0;
      for(var i=0;i<18;i++){
        a++;
        if(col-1-i<0){
          break;
        }
        if($scope.board[col-1-i][row]===false && $scope.board[col-i][row] != false){
          break;
        }
      }

      for(var i =0;i<(18-col);i++){
        b++;
        if(col+i+1>17){
          break;
        }
        if($scope.board[col+i][row]!=false && $scope.board[col+i+1][row] === false){
          break;
        }
      }

      var k=0;
      for(var i =(col-(a-1));i<(col+b);i++){
        word_vertical[k] = $scope.board[i][row];
        k++;
      } 



      var word_horizontal=[];
      var m=0;
      var n=0;
      

      for(var i=0;i<18;i++){
        m++;
        if(row-1-i<0){
          break;
        }
        if($scope.board[col][row-1-i]===false && $scope.board[col][row-i] !=false ){

          break;
        }
      }
      
      for(var i =0;i<(18-row);i++){
        n++;

        if($scope.board[col][row+i]!=false && $scope.board[col][row+i+1]===false){
          break;
        }
      }

      var j=0;
      for(var i = (row-(m-1));i<(row+n);i++){
        word_horizontal[j]=$scope.board[col][i];
        j++;

      }
        //to get all possible words of length greater than or eqaul to 2

       var word_vertical1=combine(word_vertical,2,$scope.board[col][row],(a-1),(b-1));
       var word_horizontal1=combine(word_horizontal,2,$scope.board[col][row],(m-1),(n-1));


       var array1 = [];
       var k=0;
       for(var i=0;i<word_vertical1.length;i++){
        for(var j=0;j<word_vertical1[i].length;j++){
          array1[k] = word_vertical1[i][j];
          k++;
        }
       }

       var array2 = [];
       var m=0;
         for(var i=0;i<word_horizontal1.length;i++){
        for(var j=0;j<word_horizontal1[i].length;j++){
          array2[m] = word_horizontal1[i][j];
          m++;
        }
       }
      
      var  acceptable_words_vertical = check_word(array1);
       var acceptable_words_horizontal = check_word(array2);

    

     $scope.word=acceptable_words_vertical;
     
     $scope.word1=acceptable_words_horizontal;
   

   $scope.player = $scope.player ===Player1 ? Player2 : Player1;
      value();
     

    }
    
    function setupBoard() {
     
      $scope.board = [];
      for (var i = 0; i < BOARD_SIZE; i++) {
        $scope.board[i] = [];
       
        for (var j = 0; j < BOARD_SIZE; j++) {
          
         $scope.board[i][j]=false;
        
        }
      }
      $scope.score_player1=0;
      $scope.score_player2=0;

   }
    setupBoard();

   
var combine = function(a,min,val,m,n){
  var all=[];
  
  var length = a.length;
  var index = m;
  //all elements of length 
  while(index>=0){
    var array = [];
    array[0]=a[index]
    for(var i=(index+1);i<=m;i++){
      array[0]=array[0]+a[i];
    }
    
    var j =1;
    for(var i =(m+1);i<(m+n+1);i++){
      array[j]=array[j-1]+a[i];
      j++;
    }
    all.push(array);
   
    index=index-1;
  }
     
return all;
}
  var check_word = function(a){
     var array= [] ;
     $http.get('dictionary_mod.txt').then(function(response){
    var x =response.data;
    
    var j=0;
    for(var i =0; i<a.length;i++){
      var word1 = a[i].toUpperCase();
      var word = "1"+word1+"1";
     
      if(x.indexOf(word)>=0){
        array[j]=a[i];
        j++;
      
      }
    }

    var max =0;
    for(var i=0;i<array.length;i++){
      if(array[i].length>=max){
         max=array[i].length;
      }
    } 

     
    if($scope.player===Player2){
        $scope.score_player1=$scope.score_player1+max;
      }
    else if($scope.player===Player1){
        $scope.score_player2=$scope.score_player2+max;
      }


  });
     
     return array;
  }  
     

  $scope.endGame = function(){
   
    if($scope.score_player1>$scope.score_player2){
      alert("player1 wins the game");
    }
    else if($scope.score_player2>$scope.score_player1){
      alert("player2 wins the game");
    }
    else{
      alert("game is a draw");
    }

      location.reload();
  }

  });


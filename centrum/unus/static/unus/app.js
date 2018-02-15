var app = angular.module('unus', []);

app.controller('unusController', function($scope){

    $scope.unusList = [{listElement: 'Hii!', done:false}];
    $scope.add = function(){
        $scope.unusList.push({listElement: $scope.IndexInput, done:false});
        $scope.IndexInput = '';
    };

    $scope.remove = function(){
        var oldList = $scope.unusList;
        $scope.unusList = [];
        angular.forEach(oldList, function(x) {
            if (!x.done) $scope.unusList.push(x);
        })
    }
});
var app = angular.module('unus', []);

app.controller('unusController', function($scope){

    $scope.unusList = [{name: 'Hii!'}];
    $scope.add = function(){
        $scope.unusList.push({name: $scope.IndexInput});
        $scope.IndexInput = '';
    };
});


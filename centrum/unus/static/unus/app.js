var app = angular.module('unus', []);

app.controller('unusController', function($scope, $http){

    // $scope.unusList = [{listElement: 'Hii!', done:false}];
    $http.get('/api').then(function(response){
        $scope.unusList = [];
        for (var i = 0; i< response.data.length; i++) {
            
            var list = {};
            list.name = response.data[i].list_element
            list.done = response.data[i].done
            list.id   = response.data[i].id
            $scope.unusList.push(list);
        }
    });

    $scope.saveData = function() {
        var data = {list_element: $scope.IndexInput, done: false}
        $http.put('/api', data)

        if (data.list_element != "")
            location.reload();
    }

    $scope.add = function(){
        $scope.unusList.push({listElement: $scope.IndexInput, done:false});
        $scope.IndexInput = '';
    };

    $scope.remove = function(){
        var oldList = $scope.unusList;
        $scope.unusList = [];
        angular.forEach(oldList, function(x) {
            if (x.done) {
                $http.delete('/api/' + x.id + '')
            }
            location.reload();
            $scope.unusList.push(x);
        })
    }
});
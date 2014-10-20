app = angular.module('stamps', [])

app.controller('SearchCtrl', ($scope, $http) ->
    $scope.results = []
    $scope.filters = {
        limit: 15
    }

    $scope.countries = []
    $scope.themes = []

    $http.get('/api/countries').success((data) ->
        $scope.countries = data.countries
        console.log(data)
    )

    $http.get('/api/themes').success((data) ->
        $scope.themes = data.themes
        console.log(data)
    )


    search = (new_val, old_val, scope) ->
        $http.post('/api/search', $scope.filters).success((data) ->
            console.log($scope.filters)
            $scope.results = data
            console.log(data)
        )

    $scope.$watchCollection('filters', search)
)

app = angular.module 'stamps', []

app.controller 'SearchCtrl', ($scope, $http) ->
    $scope.results = {
        count: 0
    }
    $scope.stamps = []
    $scope.busy = true
    $scope.filters = {
        limit: 9,
        skip: 0
    }

    $scope.countries = []
    $scope.themes = []
    $scope.years = [2002..2014]
    $scope.years.unshift(null)

    $http.get('/api/countries').success (data) ->
        $scope.countries = data.countries
        $scope.countries.unshift(null)
        console.log(data)

    $http.get('/api/themes').success (data) ->
        $scope.themes = data.themes
        console.log(data)

    search = (new_val, old_val, scope) ->
        $scope.busy = true
        $http.post('/api/search', $scope.filters).success (data) ->
            $scope.results = data
            for stamp in data.data
                $scope.stamps.push stamp
            $scope.busy = false

    $scope.next_page = () ->
        if not $scope.busy and $scope.filters.skip < $scope.results.count - $scope.filters.limit
            $scope.filters.skip += $scope.filters.limit
            search()

    $scope.reset_search = () ->
        $scope.filters.skip = 0
        $scope.stamps = []

    $scope.$watchCollection('filters', search)


app.directive 'whenScrolled', ($window) ->
    (scope, elm, attr) ->
        win = angular.element($window)
        body = document.body
        win.bind 'scroll', () ->
            if body.scrollTop + window.innerHeight >= body.scrollHeight - 100
                scope.next_page()


app.directive 'stamp', () ->
    restrict: 'E',
    templateUrl: '/templates/ministamp.html',
    scope:
        stamp: '=',

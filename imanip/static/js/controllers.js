'use strict';

function ImanipController($scope, $http, $location) {
	$scope.effects = [];
	$scope.file = [];

	$scope.$on("fileSelected", function (event, args) {
		$scope.$apply(function () {            
			$scope.file = args.file;
		});
	});

	$scope.add_effect = function(index) {
		$scope.effects.splice(index, 0, { effect_name: 'brightness', value: 100 })
	}

	$scope.remove_effect = function(effect_index) {
		$scope.effects.splice(effect_index, 1)
	}

	$scope.upload = function() {
		$http({
			method: 'POST'
		,	url: '/upload'
		,	headers: {'Content-Type': false}
		,	transformRequest: function (data) {
				var formData = new FormData();
				formData.append("effects", angular.toJson(data.effects));
				formData.append("file", data.file);
				return formData;
			}
		,	data: { effects: $scope.effects, file: $scope.file }
		})
		.success(function(data, status, headers, config) {
			console.log(data.path)
			$scope.image = 'image/' + data.path
		});
	}
}
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class HelloApiView(APIView):
	"""Test API View."""

	serialzer_class = serializers.HelloSerializer

	def get(self, request, format=None):
		"""Returns a list of APIView features."""

		an_apiview = [
			'Uses HTTP mehtods as function (get, post, patch, put, delete)',
			'It is similat to a traditional Django view',
			'Gives you the most controlover your logic',
			'Is mapped manually to URLs'

		]

		return Response({'message': 'Hello!', 'an_apiview': an_apiview})


	def post(self, request):
		"""Create a hello message with our name."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serialzer.is_valid():
			name = serialzer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})

		else:
			return Response(
				serialzer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		"""Handles updating an object."""


		return Response({'method': 'put'})


	def patch(self, request, pk=None):
		"""Patch request, only updates fields provided in the reques."""

		return Response({'method':'patch'})

	def delete(self, request, pk=None):
		"""Deletes an object."""

		return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet."""

	def list(self, request):
		"""Return a hello message."""

		serializer_class = serializers.HelloSerializer

		a_viewset = [
			'Uses actions (list, create, retrieve, update, partial_update)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code.'
		]

		return Response({'message' : 'Hello!', 'a_viewset': a_viewset})

	def create(self, request):
		"""Create a new hello message."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(
				serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""Handles getting an object by its ID."""

		return Response({'http_method': 'GET'})


	def update(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'http_method': 'PUT'})

	def partial_update(self, request, pk=None):
		"""Handles updating part of an object."""

		return Response({'http_method': 'PATCH'})

	def destroy(self, request, pk=None):
		"""Handles removing an object."""

		return Response({'http_method':'DELETE'})

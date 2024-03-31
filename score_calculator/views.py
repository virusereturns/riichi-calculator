from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np

from .serializers import ScoreInputSerializer
from .utils import calculate_score


class ScoreCalcAPI(APIView):
    def post(self, request):
        serializer = ScoreInputSerializer(data=request.data)
        if serializer.is_valid():
            han = serializer.validated_data['han']
            fu = serializer.validated_data['fu']
            is_dealer = serializer.validated_data['is_dealer']
            kiriage = serializer.validated_data['kiriage']
            honba = serializer.validated_data['honba']
            score_dict = calculate_score(han, fu, is_dealer, kiriage, honba)
            return Response(score_dict)
        else:
            return Response(serializer.errors, status=400)


class ScoreCalcHTMXView(TemplateView):
    template_name = 'score_calculator/_score_div.html'

    def post(self, request):
        serializer = ScoreInputSerializer(data=request.POST)
        if serializer.is_valid():
            han = serializer.validated_data['han']
            fu = serializer.validated_data['fu']
            is_dealer = serializer.validated_data['is_dealer']
            kiriage = serializer.validated_data['kiriage']
            honba = serializer.validated_data['honba']
            score_dict = calculate_score(han, fu, is_dealer, kiriage, honba)
            return render(request, self.template_name, score_dict)
        else:
            return render(request, self.template_name, {'errors': serializer.errors})


class ScoreCalcView(TemplateView):
    template_name = 'score_calculator/score_calculator.html'

    def get_context_data(self, **kwargs: Any) -> dict:
        attrs = ",".join([f"[name='{name}']" for name in ['han', 'fu', 'is_dealer', 'kiriage', 'honba']])
        kwargs['attrs'] = attrs
        return super().get_context_data(**kwargs)
